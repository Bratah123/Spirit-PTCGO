from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_until_effect
from spirit.game.card_effects.pokemon import shred
from spirit.game.card_effects.sm5 import timeless_gx

card = PokemonCardDef(
    guid="07d5d4e7-a6a8-59f9-95d1-06eb97c87389",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DialgaGX.Name",
    display_name="Dialga-GX",
    searchable_by=["Dialga-GX", "Basic", "GX", "DialgaGX"],
    subtypes=["Basic", "GX"],
    collector_number=146,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=483,
    abilities=[
        Attack(
            title="Overclock",
            game_text="Draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.METAL: 1},
            # STUB: attack effect not implemented
            effect=draw_until_effect(6),
        ),
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            # STUB: attack effect not implemented
            effect=shred,
        ),
        Attack(
            title="Timeless-GX",
            game_text="Take another turn after this one. (Skip the between-turns step.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=timeless_gx,
        ),
    ],
)