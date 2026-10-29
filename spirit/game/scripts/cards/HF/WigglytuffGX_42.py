from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.sm3 import tapu_wilderness_gx

card = PokemonCardDef(
    guid="99b4c70e-f439-56cb-bb8d-6b371d5bec05",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WigglytuffGX.Name",
    display_name="Wigglytuff-GX",
    searchable_by=["Wigglytuff-GX", "Stage 1", "GX", "WigglytuffGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=42,
    set_code="HF",
    rarity=Rarities.RareHoloGX,
    hp=210,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    family_id=39,
    abilities=[
        Attack(
            title="Rolling Rush",
            game_text="Flip a coin until you get tails. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=flip_damage(until_tails=True, bonus_per_heads=30),
        ),
        Attack(
            title="Lovely Star-GX",
            game_text="Heal all damage from this Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=tapu_wilderness_gx,
        ),
    ],
)