from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.scripts.cards.SM2.DrampaGX_115 import big_wheel_gx

from spirit.game.card_effects.sm10 import (
    shinobi_mastery,
)

card = PokemonCardDef(
    guid="817ea226-e05a-51df-a3ce-ab44a6c06f7e",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VenomothGX.Name",
    display_name="Venomoth-GX",
    searchable_by=["Venomoth-GX", "Stage 1", "GX", "VenomothGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=193,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name",
    family_id=48,
    abilities=[
        Attack(
            title="Shinobi Mastery",
            game_text="If you played Koga's Trap from your hand during this turn, this attack does 90 more damage. If you played Janine from your hand during this turn, prevent all damage done to this Pok\u00e9mon by attacks from Basic Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            damage_operator="+",
            effect=shinobi_mastery
        ),
        Attack(
            title="Ten-Card Return-GX",
            game_text="Shuffle your hand into your deck. Then, draw 10 cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=big_wheel_gx,
        ),
    ],
)