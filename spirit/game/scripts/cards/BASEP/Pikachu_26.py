from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


card = PokemonCardDef(
    guid="3434fa15-de6d-5eae-9900-bdbb7a4cb0fc",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy cards attached to Pikachu.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=40,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)
