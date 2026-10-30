from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.ex import flip_attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card

card = PokemonCardDef(
    guid="38f39a28-dc01-570d-aba1-d6db7fe3a901",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latiosex.Name",
    display_name="Latios ex",
    searchable_by=["Latios ex", "Basic", "ex", "Latiosex"],
    subtypes=["Basic", "ex"],
    collector_number=94,
    set_code="EX3",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.GRASS,
    family_id=381,
    abilities=[
        Attack(
            title="Energy Stream",
            game_text="Flip a coin. If heads, search your discard pile for a basic Energy card and attach it to Latios ex.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=flip_attach_from_discard(predicate=is_basic_energy_card),
        ),
        Attack(
            title="Luster Purge",
            game_text="Discard 3 Energy attached to Latios ex.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            # STUB: attack effect not implemented
            effect=self_energy_discard_attack(count=3),
        ),
    ],
)