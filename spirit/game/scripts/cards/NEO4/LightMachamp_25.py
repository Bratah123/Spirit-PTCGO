from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import beatdown, tag_team


card = PokemonCardDef(
    guid="207a05eb-1fad-5de7-a29a-2e755b3a6a0e",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightMachamp.Name",
    display_name="Light Machamp",
    searchable_by=["Light Machamp", "Stage 2", "LightMachamp"],
    subtypes=["Stage 2"],
    collector_number=25,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LightMachoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Tag Team",
            game_text="When you play Light Machamp from your hand, if it is on your Bench, remove 3 damage counters from your Active Pok\u00e9mon. If it has fewer damage counters than that, remove all of them. Then, switch Light Machamp with your Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_EVOLVE,
            effect=tag_team,
        ),
        Attack(
            title="Beatdown",
            game_text="If the Defending Pok\u00e9mon has Dark in its name or is a Darkness Pok\u00e9mon, flip a coin. If heads, this attack does 100 damage instead of 50.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=50,
            effect=beatdown,
        ),
    ],
)
