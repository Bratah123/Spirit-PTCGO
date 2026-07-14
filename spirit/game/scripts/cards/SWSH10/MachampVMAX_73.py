from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import bonus_if


def _bench_has_damage(ctx):
    return any(p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p) for p in ctx.my_bench())

card = PokemonCardDef(
    guid="dfb9d6ba-8009-5ad8-a787-557811761e37",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MachampVMAX.Name",
    display_name="Machamp VMAX",
    searchable_by=["Machamp VMAX", "VMAX", "MachampVMAX"],
    subtypes=["VMAX"],
    collector_number=73,
    set_code="SWSH10",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MachampV.Name",
    family_id=68,
    abilities=[
        Attack(
            title="Revenge Buster",
            game_text="If your Benched Pok\u00e9mon have any damage counters on them, this attack does 140 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=bonus_if(_bench_has_damage, 140),
        ),
        Attack(
            title="G-Max Chi Strike",
            game_text="During your next turn, this Pok\u00e9mon can't use G-Max Chi Strike.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=240,
            locks_next_turn=True,
        ),
    ],
)