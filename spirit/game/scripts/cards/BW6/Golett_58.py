from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="2a8a0057-b7f6-5d51-b40a-f65591980519",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    display_name="Golett",
    searchable_by=["Golett", "Basic", "Golett"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="BW6",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    family_id=622,
    abilities=[
        Attack(
            title="Nap",
            game_text="Heal 40 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=heal_attack(40),
        ),
        Attack(
            title="Pound",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)