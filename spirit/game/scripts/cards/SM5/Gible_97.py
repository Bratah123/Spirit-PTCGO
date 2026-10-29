from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm5 import rock_hiding_passive

card = PokemonCardDef(
    guid="88988863-e2e8-5588-89a6-39afe03d6f3b",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name",
    display_name="Gible",
    searchable_by=["Gible", "Basic", "Gible"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=443,
    abilities=[
        Ability(
            title="Rock Hiding",
            game_text="If this Pok\u00e9mon has any Fighting Energy attached to it, it has no Retreat Cost.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=rock_hiding_passive,
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)