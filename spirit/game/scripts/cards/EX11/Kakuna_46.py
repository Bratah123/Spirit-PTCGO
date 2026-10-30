"""STUB: effect not implemented — do not guess mechanics.
Kakuna (EX11 #46): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_evolution_pokemon


card = PokemonCardDef(
    guid="fd2bc85c-51f6-5dea-9edc-71384f4a1bd1",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    display_name="Kakuna",
    searchable_by=["Kakuna", "Stage 1", "Kakuna"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name",
    family_id=13,
    abilities=[
        Attack(
            title="Fast Evolution",
            game_text="Search your deck for an Evolution card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=search_to_hand(is_evolution_pokemon, prompt='Choose an Evolution card to put into your hand.'),
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)