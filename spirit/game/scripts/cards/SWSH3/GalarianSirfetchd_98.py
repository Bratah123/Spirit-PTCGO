from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.legal_actions import LOCK_UNTIL_LEAVES_ACTIVE


async def meteor_assault(ctx):
    """180. Can't use Meteor Assault again until this Pokemon leaves Active."""
    await ctx.deal_damage()
    ctx.session.turn_state.attack_locks[
        (ctx.attacker.entity_id, ctx.ability.ability_id)
    ] = LOCK_UNTIL_LEAVES_ACTIVE


card = PokemonCardDef(
    guid="03a18e8d-0e6f-50db-a4cc-2bad0044ca7f",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSirfetchd.Name",
    display_name="Galarian Sirfetch'd",
    searchable_by=["Galarian Sirfetch'd", "Stage 1", "GalarianSirfetchd"],
    subtypes=["Stage 1"],
    collector_number=98,
    set_code="SWSH3",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianFarfetchd.Name",
    family_id=865,
    abilities=[
        Attack(
            title="Pierce",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
        Attack(
            title="Meteor Assault",
            game_text="This Pok\u00e9mon can't use Meteor Assault again until it leaves the Active Spot.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=meteor_assault,
        ),
    ],
)