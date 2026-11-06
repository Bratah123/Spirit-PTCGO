from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack, ignore_effects_attack


card = PokemonCardDef(
    guid="83b30668-912e-56b6-8bad-4ba31b49d72e",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CobalionEX.Name",
    display_name="Cobalion-EX",
    searchable_by=["Cobalion-EX", "Basic", "EX", "CobalionEX"],
    subtypes=["Basic", "EX"],
    collector_number=93,
    set_code="BW8",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=638,
    abilities=[
        Attack(
            title="Righteous Edge",
            game_text="Discard a Special Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            effect=discard_opponent_energy_attack(special_only=True),
        ),
        Attack(
            title="Steel Bullet",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=ignore_effects_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)