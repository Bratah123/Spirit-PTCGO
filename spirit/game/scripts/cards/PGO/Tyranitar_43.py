from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import damage_per, spread_damage


def _bench_damage_counters(ctx) -> int:
    total = 0
    for pokemon in ctx.my_bench():
        total += max(0, (ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10)
    return total


card = PokemonCardDef(
    guid="8a6c5a53-4506-57a5-872d-916c35b27518",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name",
    display_name="Tyranitar",
    searchable_by=["Tyranitar", "Stage 2", "Tyranitar"],
    subtypes=["Stage 2"],
    collector_number=43,
    set_code="PGO",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Raging Crash",
            game_text="This attack does 10 damage for each damage counter on all of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=damage_per(_bench_damage_counters, 10),
        ),
        Attack(
            title="Earthquake",
            game_text="This attack also does 20 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=spread_damage(20, side="mine", also_base=True),
        ),
    ],
)