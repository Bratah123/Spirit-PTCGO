from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="7b7fa355-0687-5c42-97f2-67ec7fd6098c",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hattrem.Name",
    display_name="Hattrem",
    searchable_by=["Hattrem", "Stage 1", "Hattrem"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hatenna.Name",
    family_id=856,
    abilities=[
        Attack(
            title="Spiral Drain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=heal_attack(30, target="self"),
        ),
    ],
)