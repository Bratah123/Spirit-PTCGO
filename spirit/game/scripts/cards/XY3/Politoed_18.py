from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import attack_discount_passive
from spirit.game.content.definitions import def_for


def _named(card, *names):
    d = def_for(card.archetype_id)
    return getattr(d, "display_name", None) in names


card = PokemonCardDef(
    guid="49c5dde7-5222-5894-b399-716edb5f95ed",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Politoed.Name",
    display_name="Politoed",
    searchable_by=["Politoed", "Stage 2", "Politoed"],
    subtypes=["Stage 2"],
    collector_number=18,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=60,
    abilities=[
        Ability(
            title="King's Song",
            game_text="Ignore all Colorless Energy in the attack cost of each of your Poliwag, Poliwhirl, and Poliwrath's attacks.",
            passive=attack_discount_passive(99, self_only=False,
                pred=lambda p: _named(p, "Poliwag", "Poliwhirl", "Poliwrath")),
        ),
        Attack(
            title="Hyper Voice",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)