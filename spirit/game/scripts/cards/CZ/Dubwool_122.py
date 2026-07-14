from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage, snipe_attack

card = PokemonCardDef(
    guid="78aee80e-9456-52a3-b2e2-55268181d44b",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dubwool.Name",
    display_name="Dubwool",
    searchable_by=["Dubwool", "Stage 1", "Dubwool"],
    subtypes=["Stage 1"],
    collector_number=122,
    set_code="CZ",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wooloo.Name",
    family_id=831,
    abilities=[
        Attack(
            title="Overhead Throw",
            game_text="This attack also does 10 damage to 1 of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=snipe_attack(10, pool="bench", count=1, side="mine", also_base=True),
        ),
        Attack(
            title="Rolling Dash",
            game_text="Flip a coin until you get tails. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=flip_damage(until_tails=True, base=60, per_heads=30),
        ),
    ],
)