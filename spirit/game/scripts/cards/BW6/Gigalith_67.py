from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import recoil_attack, damage_per


def _bench_counters(ctx):
    total = 0
    for pokemon in ctx.my_bench():
        total += max(0, ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10
    return total


card = PokemonCardDef(
    guid="f7f91df0-101e-51ab-81bd-7122c3247cc9",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gigalith.Name",
    display_name="Gigalith",
    searchable_by=["Gigalith", "Stage 2", "Gigalith"],
    subtypes=["Stage 2"],
    collector_number=67,
    set_code="BW6",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Boldore.Name",
    family_id=524,
    abilities=[
        Attack(
            title="Revenge Cannon",
            game_text="Does 10 more damage for each damage counter on each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(_bench_counters, 10, base=10),
        ),
        Attack(
            title="Reckless Charge",
            game_text="This Pok\u00e9mon does 40 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=recoil_attack(40),
        ),
    ],
)