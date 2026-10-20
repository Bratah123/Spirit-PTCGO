from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack
from spirit.game.card_effects.passives_common import TypedDamageBoostPassive


card = PokemonCardDef(
    guid="8b159553-c2bd-5c49-b00a-3fcc70b98d27",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalant.Name",
    display_name="Bouffalant",
    searchable_by=["Bouffalant", "Basic", "Bouffalant"],
    subtypes=["Basic"],
    collector_number=119,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=626,
    abilities=[
        Ability(
            title="Sap Sipper",
            game_text="This Pok\u00e9mon's attacks do 40 more damage to your opponent's Grass Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=TypedDamageBoostPassive(PokemonTypes.GRASS, 40, to_active_only=False),
        ),
        Attack(
            title="Derail",
            game_text="Discard a Special Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=discard_opponent_energy_attack(special_only=True),
        ),
    ],
)