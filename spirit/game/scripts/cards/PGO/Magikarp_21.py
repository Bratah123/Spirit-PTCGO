from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.attacks_common import damage_per, count_discard


def _is_magikarp(card):
    return card.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Magikarp"


def _is_magikarp_or_gyarados(card):
    return card.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) in ("Magikarp", "Gyarados")

card = PokemonCardDef(
    guid="9c7cea7e-3a5f-51fd-9b32-4edaa5613811",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    display_name="Magikarp",
    searchable_by=["Magikarp", "Basic", "Magikarp"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="PGO",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Attack(
            title="Lively Grouping",
            game_text="Search your deck for any number of Magikarp, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(_is_magikarp, count=60, minimum=0, reveal=True),
        ),
        Attack(
            title="Raging Fin",
            game_text="This attack does 30 more damage for each Magikarp and Gyarados in your discard pile.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_discard("mine", pred=_is_magikarp_or_gyarados), 30, base=10),
        ),
    ],
)