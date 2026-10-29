from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm12 import supreme_puff_gx
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="27817b53-38bb-5f4f-939d-811d90242ea6",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TogepiCleffaIgglybuffGX.Name",
    display_name="Togepi & Cleffa & Igglybuff-GX",
    searchable_by=["Togepi & Cleffa & Igglybuff-GX", "Basic", "TAG TEAM", "GX", "TogepiCleffaIgglybuffGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=272,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    hp=240,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=173,
    abilities=[
        Attack(
            title="Rolling Panic",
            game_text="Flip a coin until you get tails. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=flip_damage(until_tails=True, bonus_per_heads=30),
        ),
        Attack(
            title="Supreme Puff-GX",
            game_text="Take another turn after this one. (Skip the between-turns step.) If this Pok\u00e9mon has at least 14 extra Fairy Energy attached to it (in addition to this attack's cost), your opponent shuffles all of their Benched Pok\u00e9mon and all cards attached to them into their deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 2},
            effect=supreme_puff_gx,
        ),
    ],
)