from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.session.passives import Passive
from spirit.game.models.board import BoardState
from spirit.game.card_effects.pokemon import energy_provides_type


def _has_grass_energy(pokemon) -> bool:
    return any(
        energy_provides_type(e, PokemonTypes.GRASS.value)
        for e in BoardState.attached_energies(pokemon)
    )


class CurativeBowerPassive(Passive):
    def blocks_special_conditions(self, target, condition, carrier):
        if condition != SpecialConditions.CONFUSED:
            return False
        if target is None or target.owning_player_id != carrier.owning_player_id:
            return False
        return _has_grass_energy(target)


async def curative_bower_cure(ctx):
    """Cures Confusion on any of your Pokemon that already have Grass Energy attached."""
    for pokemon in ctx.my_pokemon_in_play():
        if _has_grass_energy(pokemon):
            await ctx.cure_condition(pokemon, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="d2fa901f-fe1a-5efe-86d2-b4bb082f952f",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tropius.Name",
    display_name="Tropius",
    searchable_by=["Tropius", "Basic", "Tropius"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=357,
    abilities=[
        Ability(
            title="Curative Bower",
            game_text="All of your Pok\u00e9mon that have Grass Energy attached can't be Confused, and if they are already Confused, they recover from that Special Condition.",
            passive=CurativeBowerPassive(),
            trigger=(Triggers.ON_PLAY, Triggers.ON_ENERGY_ATTACHED),
            effect=curative_bower_cure,
        ),
        Attack(
            title="Slicing Blade",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)