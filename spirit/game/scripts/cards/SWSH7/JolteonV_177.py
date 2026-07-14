from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage, snipe_attack

card = PokemonCardDef(
    guid="d83e599d-ff36-59e0-8fa9-bfc406c83c85",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.JolteonV.Name",
    display_name="Jolteon V",
    searchable_by=["Jolteon V", "Basic", "V", "JolteonV"],
    subtypes=["Basic", "V"],
    collector_number=177,
    set_code="SWSH7",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=135,
    abilities=[
        Attack(
            title="Thunder Spear",
            game_text="This attack does 20 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(20, pool="any", count=1),
        ),
        Attack(
            title="Pin Missile",
            game_text="Flip 4 coins. This attack does 60 damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=60),
        ),
    ],
)