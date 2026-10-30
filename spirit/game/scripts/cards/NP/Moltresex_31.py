from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import synchronized_lift_passive, may_move_own_energy
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


card = PokemonCardDef(
    guid="2e366da7-6668-5fdf-b439-dd7ea35bb7d7",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltresex.Name",
    display_name="Moltres ex",
    searchable_by=["Moltres ex", "Basic", "ex", "Moltresex"],
    subtypes=["Basic", "ex"],
    collector_number=31,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=146,
    abilities=[
        Ability(
            title="Synchronized Lift",
            game_text="As long as you have Articuno ex and Zapdos ex in play, the Retreat Cost for Moltres ex is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=synchronized_lift_passive("Articuno ex", "Zapdos ex"),
        ),
        Attack(
            title="Flame Gift",
            game_text="You may move a Fire Energy card attached to Moltres ex to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=may_move_own_energy(PokemonTypes.FIRE),
        ),
        Attack(
            title="Scorching Wing",
            game_text="Discard all Fire Energy attached to Moltres ex.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=self_energy_discard_attack(
                all_energy=True, energy_type=PokemonTypes.FIRE),
        ),
    ],
)
