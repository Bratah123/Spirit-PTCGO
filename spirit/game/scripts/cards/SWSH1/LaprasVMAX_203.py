from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy

card = PokemonCardDef(
    guid="534ba9ef-f878-546c-90c2-9fc6659ad1e2",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LaprasVMAX.Name",
    display_name="Lapras VMAX",
    searchable_by=["Lapras VMAX", "VMAX", "LaprasVMAX"],
    subtypes=["VMAX"],
    collector_number=203,
    set_code="SWSH1",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LaprasV.Name",
    family_id=131,
    abilities=[
        Attack(
            title="G-Max Pump",
            game_text="This attack does 30 more damage for each Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            damage_operator="+",
            effect=damage_per(
                count_energy("self", energy_type=PokemonTypes.WATER), 30, base=90
            ),
        ),
    ],
)