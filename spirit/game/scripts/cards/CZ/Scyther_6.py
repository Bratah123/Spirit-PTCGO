from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack

card = PokemonCardDef(
    guid="b6551aa8-2839-5327-a3a3-d59bb2425325",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    display_name="Scyther",
    searchable_by=["Scyther", "Basic", "Scyther"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="CZ",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=123,
    abilities=[
        Attack(
            title="Mach Cut",
            game_text="Discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=discard_opponent_energy_attack(count=1, special_only=True),
        ),
    ],
)