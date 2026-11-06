from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import SlipperySkinPassive


card = PokemonCardDef(
    guid="5b60d2b8-a55f-576d-b966-4cf36dbe07a7",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dunsparce.Name",
    display_name="Dunsparce",
    searchable_by=["Dunsparce", "Basic", "Dunsparce"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=206,
    abilities=[
        Ability(
            title="Slippery Skin",
            game_text="As long as the Defending Pok\u00e9mon is an Evolved Pok\u00e9mon, Dunsparce's Retreat Cost is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=SlipperySkinPassive(),
        ),
        Attack(
            title="Tail Shake",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
