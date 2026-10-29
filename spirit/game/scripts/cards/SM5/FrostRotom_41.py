from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm5 import RotoMotorPassive, frost_crush

card = PokemonCardDef(
    guid="a4e360d8-bae8-5574-99d3-4f28cf5e8133",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FrostRotom.Name",
    display_name="Frost Rotom",
    searchable_by=["Frost Rotom", "Basic", "FrostRotom"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=479,
    abilities=[
        Ability(
            title="Roto Motor",
            game_text="If you have 9 or more Pok\u00e9mon Tool cards in your discard pile, ignore all Energy in the attack cost of each of this Pok\u00e9mon's attacks.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=RotoMotorPassive(),
        ),
        Attack(
            title="Frost Crush",
            game_text="This attack does 20 more damage times the amount of Energy attached to all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=frost_crush,
        ),
    ],
)