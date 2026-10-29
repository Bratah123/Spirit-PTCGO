from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.sm7 import (
    chuck_away,
    item_maniac_gx,
)


card = PokemonCardDef(
    guid="4824d5ee-f116-5f35-ad3a-2d99e10b2df4",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRaticateGX.Name",
    display_name="Alolan Raticate-GX",
    searchable_by=["Alolan Raticate-GX", "Stage 1", "GX", "AlolanRaticateGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=85,
    set_code="SM7",
    rarity=Rarities.RareHoloGX,
    hp=200,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRattata.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Chuck Away",
            game_text="Discard up to 2 cards from your hand. This attack does 40 damage for each card you discarded in this way.",
            cost={},
            damage=40,
            damage_operator="x",
            effect=chuck_away,
        ),
        Attack(
            title="Hyper Fang",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            # STUB: attack effect not implemented
            effect=flip_or_nothing(),
        ),
        Attack(
            title="Item Maniac-GX",
            game_text="Search your deck for up to 6 Item cards, reveal them, and put them into your hand. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={},
            effect=item_maniac_gx,
        ),
    ],
)