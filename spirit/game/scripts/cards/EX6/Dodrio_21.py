from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ex import retreat_aid_passive


card = PokemonCardDef(
    guid="9b158d5e-79b9-551b-bef9-916f84d31e96",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dodrio.Name",
    display_name="Dodrio",
    searchable_by=["Dodrio", "Stage 1", "Dodrio"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="EX6",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name",
    family_id=84,
    abilities=[
        Ability(
            title="Retreat Aid",
            game_text="As long as Dodrio is on your Bench, you pay ColorlessColorless less to retreat your Active Pok\u00e9mon (excluding Pok\u00e9mon-ex and Baby Pok\u00e9mon.)",
            ability_type=AbilityTypes.POKE_BODY,
            passive=retreat_aid_passive(),
        ),
        Attack(
            title="Tri Attack",
            game_text="Flip 3 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=20),
        ),
    ],
)