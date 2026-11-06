from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.ecard import is_benched, rock_tumble
from spirit.game.card_effects.support_common import remove_self_from_play


card = PokemonCardDef(
    guid="15462835-1263-5fb4-a074-089268121b24",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name",
    display_name="Azumarill",
    searchable_by=["Azumarill", "Stage 1", "Azumarill"],
    subtypes=["Stage 1"],
    collector_number=154,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    family_id=183,
    abilities=[
        Ability(
            title="Bubble Turn",
            game_text="Once during your turn (before your attack), if Azumarill is on your Bench, you may flip a coin. If heads, return Azumarill and all cards attached to it to your hand.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=is_benched,
            effect=flip_or_nothing(then=remove_self_from_play()),
        ),
        Attack(
            title="Aqua Sonic",
            game_text="Don't apply Resistance.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=rock_tumble,
        ),
    ],
)
