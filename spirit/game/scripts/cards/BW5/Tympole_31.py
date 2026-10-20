from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="376a163c-949f-5035-9a8e-ec6aef968e67",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tympole.Name",
    display_name="Tympole",
    searchable_by=["Tympole", "Basic", "Tympole"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="BW5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=535,
    abilities=[
        Attack(
            title="Spiral Drain",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=heal_attack(20),
        ),
    ],
)