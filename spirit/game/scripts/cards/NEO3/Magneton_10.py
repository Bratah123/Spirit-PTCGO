from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.pokemon import is_lightning_energy
from spirit.game.card_effects.ecard import (
    electromagnetic_power,
    electromagnetic_power_condition,
)


card = PokemonCardDef(
    guid="2b18e8ea-c91f-53ea-8145-4d61fc14bdf0",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    display_name="Magneton",
    searchable_by=["Magneton", "Stage 1", "Magneton"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="NEO3",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    family_id=82,
    abilities=[
        Ability(
            title="Electromagnetic Power",
            game_text="As often as you like during your turn (before your attack), you may take 1 Energy card attached to 1 of your Magnemites, Magnetons, or Dark Magnetons and attach it to a different 1 of your Magnemites, Magnetons, and Dark Magnetons. This power can't be used if Magneton is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.UNLIMITED,
            condition=electromagnetic_power_condition,
            effect=electromagnetic_power,
        ),
        Attack(
            title="Plasma",
            game_text="If there are any Lightning Energy cards in your discard pile, attach 1 of them to Magneton.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=attach_from_discard(predicate=is_lightning_energy),
        ),
    ],
)
