from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm3 import tapu_wilderness_gx
from spirit.game.card_effects.sm7 import (
    breakdown,
    magic_evens_passive,
)


card = PokemonCardDef(
    guid="5807ed97-2507-57a3-87fc-3e7595003124",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMimeGX.Name",
    display_name="Mr. Mime-GX",
    searchable_by=["Mr. Mime-GX", "Basic", "GX", "MrMimeGX"],
    subtypes=["Basic", "GX"],
    collector_number=156,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=122,
    abilities=[
        Ability(
            title="Magic Evens",
            game_text="Prevent all damage done to this Pok\u00e9mon by your opponent's attacks if that damage is exactly 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, or 260.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=magic_evens_passive,
        ),
        Attack(
            title="Breakdown",
            game_text="For each card in your opponent's hand, put 1 damage counter on their Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=breakdown,
        ),
        Attack(
            title="Life Trick-GX",
            game_text="Heal all damage from this Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=tapu_wilderness_gx,
        ),
    ],
)