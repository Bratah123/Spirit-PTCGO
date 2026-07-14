from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="a3f770e9-2819-5ab9-835a-36f3df1a8a66",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirVMAX.Name",
    display_name="Gardevoir VMAX",
    searchable_by=["Gardevoir VMAX", "VMAX", "GardevoirVMAX"],
    subtypes=["VMAX"],
    collector_number=76,
    set_code="SWSH35",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirV.Name",
    family_id=282,
    abilities=[
        Attack(
            title="Max Cure",
            game_text="Heal 50 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=heal_attack(50),
        ),
    ],
)