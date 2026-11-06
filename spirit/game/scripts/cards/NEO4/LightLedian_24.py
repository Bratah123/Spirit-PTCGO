from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import flash_touch


card = PokemonCardDef(
    guid="7121754c-1af5-5311-abea-f9d67c0073c7",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightLedian.Name",
    display_name="Light Ledian",
    searchable_by=["Light Ledian", "Stage 1", "LightLedian"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ledyba.Name",
    family_id=165,
    abilities=[
        Attack(
            title="Flash Touch",
            game_text="If you have any Benched Pok\u00e9mon, switch 1 of them with Light Ledian. As long as that Pok\u00e9mon is your Active Pok\u00e9mon, it can't become Asleep, Confused, Paralyzed, or Poisoned. (All other effects of attacks, Pok\u00e9mon Powers, and Trainer cards still happen.)",
            cost={PokemonTypes.GRASS: 1},
            effect=flash_touch,
        ),
        Attack(
            title="Comet Punch",
            game_text="Flip 4 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=20),
        ),
    ],
)
