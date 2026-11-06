from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


card = PokemonCardDef(
    guid="e5254957-3f13-586e-a7c1-17c6cf81c453",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlackKyuremEX.Name",
    display_name="Black Kyurem-EX",
    searchable_by=["Black Kyurem-EX", "Basic", "EX", "BlackKyuremEX"],
    subtypes=["Basic", "EX"],
    collector_number=95,
    set_code="BW8",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DRAGON,
    family_id=646,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
        Attack(
            title="Black Ballista",
            game_text="Discard 3 Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=self_energy_discard_attack(count=3),
        ),
    ],
)