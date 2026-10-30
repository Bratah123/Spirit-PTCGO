from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Activations
from spirit.game.attributes import AttrID
from spirit.game.session.passives import effective_max_hp


def _pollen_condition(board, player_id, pokemon=None):
    return any(effective_max_hp(board, p) > p.get_attribute(AttrID.HP, 0)
               for p in board.pokemon_in_play(player_id))


async def _curative_pollen(ctx):
    """Heal 20 damage from 1 of your Pokemon."""
    pool = [p for p in ctx.my_pokemon_in_play()
            if ctx.max_hp(p) > p.get_attribute(AttrID.HP, 0)]
    if not pool:
        return
    target = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(pool, "Heal which Pokémon?")
    if target is not None:
        await ctx.heal(20, target)


card = PokemonCardDef(
    guid="83deb05d-b0ed-572c-ba17-46b7a1ebeab0",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ribombee.Name",
    display_name="Ribombee",
    searchable_by=["Ribombee", "Stage 1", "Ribombee"],
    subtypes=["Stage 1"],
    collector_number=93,
    set_code="SM1",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cutiefly.Name",
    family_id=742,
    abilities=[
        Ability(
            title="Curative Pollen",
            game_text="Once during your turn (before your attack), you may heal 20 damage from 1 of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=_pollen_condition,
            effect=_curative_pollen,
        ),
        Attack(
            title="Fairy Wind",
            cost={PokemonTypes.FAIRY: 1},
            damage=30,
        ),
    ],
)