from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack, damage_per, count_energy


_self_energy = count_energy('self')
_defender_energy = count_energy('defender')


def _x_ball_count(ctx):
    return _self_energy(ctx) + _defender_energy(ctx)


card = PokemonCardDef(
    guid="d0acc916-b2b7-5719-a451-44798ffdf136",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoEX.Name",
    display_name="Mewtwo-EX",
    searchable_by=["Mewtwo-EX", "Basic", "EX", "MewtwoEX"],
    subtypes=["Basic", "EX"],
    collector_number=98,
    set_code="BW4",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="X Ball",
            game_text="Does 20 damage times the amount of Energy attached to this Pok\u00e9mon and the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=damage_per(_x_ball_count, 20),
        ),
        Attack(
            title="Psydrive",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)