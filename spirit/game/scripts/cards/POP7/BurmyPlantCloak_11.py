from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Activations
from spirit.game.card_effects.ex import wear_cloak_attach, wear_cloak_condition, cloak_tackle_bonus

card = PokemonCardDef(
    guid="c34ebe46-8fce-5567-8fdc-dcf9928a2d08",
    key="POP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BurmyPlantCloak.Name",
    display_name="Burmy Plant Cloak",
    searchable_by=['Burmy Plant Cloak', 'Basic', 'Burmy'],
    subtypes=["Basic"],
    collector_number=11,
    set_code="POP7",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=412,
    abilities=[
        Ability(
            title="Wear Cloak",
            game_text="Once during your turn (before your attack), if Burmy Plant Cloak is your Active Pokémon, you may search your discard pile for a basic Grass Energy card and attach it to Burmy Plant Cloak.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=wear_cloak_condition(),
            effect=wear_cloak_attach(PokemonTypes.GRASS),
        ),
        Attack(
            title="Plant Cloak Tackle",
            game_text="If Burmy Plant Cloak has any Grass Energy attached to it, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=cloak_tackle_bonus(PokemonTypes.GRASS, 10, 10),
        ),
    ],
)
