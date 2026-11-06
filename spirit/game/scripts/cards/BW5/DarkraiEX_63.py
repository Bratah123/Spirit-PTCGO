from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _has_darkness_energy(pokemon, carrier):
    if pokemon.owning_player_id != carrier.owning_player_id:
        return False
    return any(is_energy_card(c) and energy_provides_type(c, PokemonTypes.DARKNESS.value)
               for c in pokemon.children)


card = PokemonCardDef(
    guid="76fb1281-09a0-54fc-a2ae-539e8002d0c7",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiEX.Name",
    display_name="Darkrai-EX",
    searchable_by=["Darkrai-EX", "Basic", "EX", "DarkraiEX"],
    subtypes=["Basic", "EX"],
    collector_number=63,
    set_code="BW5",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=491,
    abilities=[
        Ability(
            title="Dark Cloak",
            game_text="Each of your Pok\u00e9mon that has any Darkness Energy attached to it has no Retreat Cost.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=retreat_free_when(_has_darkness_energy),
        ),
        Attack(
            title="Night Spear",
            game_text="Does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=snipe_attack(30, pool='bench', count=1, also_base=True),
        ),
    ],
)