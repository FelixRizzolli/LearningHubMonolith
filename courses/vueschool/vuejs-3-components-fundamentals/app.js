
const PlanComponent = {
    template: '#plan-template',
    props: {
        name: {
            type: String,
            required: true,
        },
    }
}

const PlanPickerComponent = {
    template: '#plan-picker-template',
    data() {
        return {
            plans: [
                'The Single',
                'The Curious',
                'The Addict',
            ],
        };
    },
    components: {
        Plan: PlanComponent
    },
}

const app = Vue
    .createApp({
        components: {
            PlanPicker: PlanPickerComponent
        }
    })
    .mount('#app')