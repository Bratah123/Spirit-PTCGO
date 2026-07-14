from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack

card = PokemonCardDef(
    guid="e58dee9d-1c90-50f0-b9c5-0cd00a1c5751",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LucarioV.Name",
    display_name="Lucario V",
    searchable_by=["Lucario V", "Basic", "V", "LucarioV"],
    subtypes=["Basic", "V"],
    collector_number=78,
    set_code="SWSH10",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=448,
    abilities=[
        Attack(
            title="Crushing Punch",
            game_text="Discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=discard_opponent_energy_attack(special_only=True),
        ),
        Attack(
            title="Cyclone Kick",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)