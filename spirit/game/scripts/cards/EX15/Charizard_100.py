"""STUB: effect not implemented — do not guess mechanics.
Charizard ★ δ (EX15 #100): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import dark_swirl_discard_all_mill3, rotating_claws
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ef2fa2be-24b7-512a-95df-bc3c8cc26c8d",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard ★ δ",
    searchable_by=["Charizard \u2605 \u03b4", "Basic", "Star", "Charizard"],
    subtypes=["Basic", "Star"],
    collector_number=100,
    set_code="EX15",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=6,
    abilities=[
        Attack(
            title="Rotating Claws",
            game_text="You may discard an Energy card attached to Charizard Star. If you do, search your discard pile for an Energy card (excluding the one you discarded) and attach it to Charizard Star.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=rotating_claws(),
        ),
        Attack(
            title="Dark Swirl",
            game_text="Discard all Energy cards attached to Charizard Star and discard the top 3 cards from your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 4, PokemonTypes.COLORLESS: 1},
            damage=150,
            # STUB: attack effect not implemented
            effect=dark_swirl_discard_all_mill3(150),
        ),
    ],
)