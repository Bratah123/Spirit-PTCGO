"""EX7 Team Rocket Returns — Rocket's Scyther ex.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import bounce_switch, slashing_strike_lock, dual_armor_passive

card = PokemonCardDef(
    guid="ee3550f6-631f-5a79-ae48-ef507030d188",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsScytherex.Name",
    display_name="Rocket's Scyther ex",
    searchable_by=["Rocket's Scyther ex", "Basic", "ex", "RocketsScytherex"],
    subtypes=["Basic", "ex"],
    collector_number=102,
    set_code="EX7",
    rarity=Rarities.RareHoloEX,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=123,
    abilities=[
        Ability(
            title="Dual Armor",
            game_text="As long as Rocket's Scyther ex has any Grass Energy attached to it, Rocket's Scyther ex is both Grass and Darkness type.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=dual_armor_passive(PokemonTypes.GRASS),
            effect=None,
        ),
        Attack(
            title="Bounce",
            game_text="After your attack, you may switch Rocket's Scyther ex with 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=bounce_switch(),
        ),
        Attack(
            title="Slashing Strike",
            game_text="Rocket's Scyther ex can't use Slashing Strike during your next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=slashing_strike_lock(flip=False),
            locks_next_turn=True,
        ),
    ],
)
