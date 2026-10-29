from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm6 import abnormal_outbreak
from spirit.game.card_effects.sm5 import go_second_first_turn

card = PokemonCardDef(
    guid="b9556713-cd9e-5f74-9e89-d77af5546aca",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scatterbug.Name",
    display_name="Scatterbug",
    searchable_by=["Scatterbug", "Basic", "Scatterbug"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=664,
    abilities=[
        Ability(
            title="Abnormal Outbreak",
            game_text="You can use this Ability only if you go second. Once during your first turn (before your attack), you may search your deck for a Spewpa and a Vivillon, reveal them, and put them into your hand. Then, shuffle your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=go_second_first_turn,
            effect=abnormal_outbreak,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
        ),
    ],
)
