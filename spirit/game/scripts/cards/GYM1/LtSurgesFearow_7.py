from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage


card = PokemonCardDef(
    guid="f60db4b0-06ef-56e2-a8d4-9d352f7336ac",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesFearow.Name",
    display_name="Lt. Surge's Fearow",
    searchable_by=["Lt. Surge's Fearow", "Stage 1", "LtSurgesFearow"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesSpearow.Name",
    family_id=21,
    abilities=[
        Attack(
            title="Repeating Drill",
            game_text="Flip 5 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=5, per_heads=10),
        ),
        Attack(
            title="Clutch",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)
