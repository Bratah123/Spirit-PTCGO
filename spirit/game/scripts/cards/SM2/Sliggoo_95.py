from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.card_effects.support_common import search_to_bench

from spirit.game.session.effects import is_pokemon_card


def _is_sliggoo(card):
    return is_pokemon_card(card) and card.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Sliggoo"


card = PokemonCardDef(
    guid="43f84e89-6638-5b82-a7d2-68f883faa2ab",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name",
    display_name="Sliggoo",
    searchable_by=["Sliggoo", "Stage 1", "Sliggoo"],
    subtypes=["Stage 1"],
    collector_number=95,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Goomy.Name",
    family_id=704,
    abilities=[
        Attack(
            title="Division",
            game_text="Search your deck for up to 2 Sliggoo and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(_is_sliggoo, count=2, prompt='Choose up to 2 Sliggoo'),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FAIRY: 1},
            damage=20,
        ),
    ],
)