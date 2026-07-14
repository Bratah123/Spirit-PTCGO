from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack, bonus_if, has_damage


async def _switch_self(ctx):
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)

card = PokemonCardDef(
    guid="8b0a6d3e-8365-5861-85de-47ec0ed75b5f",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxray.Name",
    display_name="Luxray",
    searchable_by=["Luxray", "Stage 2", "Rapid Strike", "Luxray"],
    subtypes=["Stage 2", "Rapid Strike"],
    collector_number=43,
    set_code="CZ",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    family_id=403,
    abilities=[
        Attack(
            title="Electrostep",
            game_text="This attack does 40 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=snipe_attack(40, pool="any", count=1, also=_switch_self),
        ),
        Attack(
            title="Scar Strikes",
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 100 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=bonus_if(has_damage("defender"), 100),
        ),
    ],
)
