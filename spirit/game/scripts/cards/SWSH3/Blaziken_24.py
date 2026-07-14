from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.passives_common import is_in_active_spot

card = PokemonCardDef(
    guid="337f5722-020d-5675-ae97-021c8517e0f9",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blaziken.Name",
    display_name="Blaziken",
    searchable_by=["Blaziken", "Stage 2", "Blaziken"],
    subtypes=["Stage 2"],
    collector_number=24,
    set_code="SWSH3",
    rarity=Rarities.RareHolo,
    hp=170,
    # Double Type: this Pokemon is Fire AND Fighting type as long as it's in
    # play; baked directly into POKEMON_TYPES since Weakness is computed off
    # the live attacker's type list.
    elements=[PokemonTypes.FIRE, PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    family_id=255,
    abilities=[
        Ability(
            title="Double Type",
            game_text="As long as this Pokémon is in play, it is Fire and Fighting type.",
        ),
        Attack(
            title="Turbo Drive",
            game_text="Attach a basic Energy card from your discard pile to 1 of your Benched Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=attach_from_discard(
                predicate=is_basic_energy_card, count=1,
                target=lambda p: not is_in_active_spot(p),
                prompt="Choose a basic Energy card to attach to 1 of your Benched Pokémon",
            ),
        ),
    ],
)
