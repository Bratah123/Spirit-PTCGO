from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import flip_or_nothing


async def enriching_seeds(ctx):
    """Heal all damage from 1 of your Benched Pokémon."""
    bench = [p for p in ctx.my_bench()
             if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to heal")
    if target is not None:
        await ctx.heal(ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0), target)

card = PokemonCardDef(
    guid="965085fc-ce66-5cce-a9a2-98cf514b0ea9",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eldegoss.Name",
    display_name="Eldegoss",
    searchable_by=["Eldegoss", "Stage 1", "Eldegoss"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="SWSH45",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gossifleur.Name",
    family_id=829,
    abilities=[
        Attack(
            title="Enriching Seeds",
            game_text="Heal all damage from 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=enriching_seeds,
        ),
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            effect=flip_or_nothing(),
        ),
    ],
)