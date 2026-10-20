from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import retreat_discount
from spirit.game.session.effects import is_team_plasma_pokemon


def _own_plasma(pokemon, carrier):
    """Each of your Team Plasma Pokemon in play."""
    return pokemon.owning_player_id == carrier.owning_player_id and is_team_plasma_pokemon(pokemon)


card = PokemonCardDef(
    guid="f3e6c08c-70e9-5fa6-afbd-2fc8891daa6d",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glaceon.Name",
    display_name="Glaceon",
    searchable_by=["Glaceon", "Stage 1", "Team Plasma", "Glaceon"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=23,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Freeze Zone",
            game_text="The Retreat Cost of each of your Team Plasma Pok\u00e9mon in play is ColorlessColorless less.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=retreat_discount(2, _own_plasma),
        ),
        Attack(
            title="Icy Wind",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)