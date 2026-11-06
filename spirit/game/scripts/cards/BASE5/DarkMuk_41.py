from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import StickyGooPassive


card = PokemonCardDef(
    guid="d9e1997e-aed6-5bb6-aa35-160d66b81cd0",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkMuk.Name",
    display_name="Dark Muk",
    searchable_by=["Dark Muk", "Stage 1", "DarkMuk"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Sticky Goo",
            game_text="As long as Dark Muk is your Active Pok\u00e9mon, your opponent pays ColorlessColorless more to retreat his or her Active Pok\u00e9mon. This power stops working while Dark Muk is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=StickyGooPassive(),
        ),
        Attack(
            title="Sludge Punch",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
