from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import damage_per, count_energy, condition_bonus_attack


card = PokemonCardDef(
    guid="a3fcc9f0-e1c7-5521-87e8-c0eaef560158",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiEX.Name",
    display_name="Darkrai-EX",
    searchable_by=["Darkrai-EX", "Basic", "EX", "DarkraiEX"],
    subtypes=["Basic", "EX"],
    collector_number=74,
    set_code="XY9",
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
        Attack(
            title="Dark Pulse",
            game_text="This attack does 20 more damage for each Darkness Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_energy('mine', energy_type=PokemonTypes.DARKNESS), 20, base=20),
        ),
        Attack(
            title="Dark Head",
            game_text="If your opponent's Active Pok\u00e9mon is Asleep, this attack does 80 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=condition_bonus_attack(80, SpecialConditions.ASLEEP),
        ),
    ],
)